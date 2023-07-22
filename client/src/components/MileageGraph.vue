<template>
  <v-card variant="flat">
    <v-card-actions class="d-flex justify-space-between">
      <v-btn
        :class="activeButton === range ? 'bg-green' : 'text-green'"
        variant="tonal"
        v-for="range in ['This Week', 'This Month', 'This Year', 'Overall']"
        :key="range"
        rounded="xl"
        size="small"
        @click="filterData(range)"
      >
        {{ range }}
      </v-btn>
    </v-card-actions>
    <LineWithLineChart :data="graphData" :options="options" />
  </v-card>
</template>

<script setup lang="ts">
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js'
import type { ChartDataset } from 'chart.js'
import LineWithLineChart from '../types/LineWithLineChart'
import { ref, computed } from 'vue'
import type Mileage from '../types/mileage'

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend) // creating instance of chart

const labels = ref<string[]>([])
const data = ref<number[]>([])
const activeButton = ref('This Week')
const props = defineProps<{ dataPoints: Mileage[] }>()

function filterData(range: string) {
  activeButton.value = range
  let minDate
  const currentDate = new Date()

  //filtering the data based on the range selected
  if (range === 'This Week') {
    minDate = new Date(currentDate.getFullYear(), currentDate.getMonth(), currentDate.getDate() - 6)
  } else if (range === 'This Month') {
    minDate = new Date(currentDate.getFullYear(), currentDate.getMonth() - 1, currentDate.getDate())
  } else if (range === 'This Year') {
    minDate = new Date(currentDate.getFullYear() - 1, currentDate.getMonth(), currentDate.getDate())
  } else {
    minDate = props.dataPoints.reduce((min, obj) => {
      const currentDate = new Date(obj.date)
      return currentDate < min ? currentDate : min
    }, new Date())
  }

  labels.value = []
  data.value = []
  while (currentDate >= minDate) {
    const dateString = currentDate.toISOString().split('T')[0]
    // changing labels based on the range selected
    let datalabel = ''

    const day = currentDate.getDate()
    const weekday = currentDate.toLocaleString('default', { weekday: 'short' })
    const month = currentDate.toLocaleString('default', { month: 'short' })
    const year = currentDate.getFullYear()

    if (range === 'This Week') {
      datalabel = `${weekday} ${day}`
    }
    if (range === 'This Year' || range === 'This Month') {
      datalabel = `${month} ${day}`
    }
    if (range === 'Overall') {
      datalabel = `${month} ${day}, ${year}`
    }

    //making sure dates that don't exist in the database are still included as 0 km
    const km = props.dataPoints.reduce((acc, cur) => cur.date === dateString ? acc + cur.kilometres : acc, 0)
    labels.value.unshift(datalabel)
    data.value.unshift(km)
    currentDate.setDate(currentDate.getDate() - 1)
  }
}

filterData('This Week')

// GRAPH DATA
const graphData = computed(() => {
  return {
    type: 'line',
    labels: labels.value,
    datasets: [
      {
        data: data.value
      } as ChartDataset<'line', (number | null)[]> // Update the type assertion
    ]
  }
})

// GRAPH CONFIGURATION
const options = {
  borderColor: 'rgb(255, 99, 99)',
  fill: false,
  cubicInterpolationMode: 'monotone',
  lineTension: 0.8,
  responsive: true,
  maintainAspectRatio: true,
  plugins: {
    legend: {
      display: false
    }
  },
  scales: {
    x: {
      grid: {
        display: false
      }
    },
    y: {
      beginAtZero: true,
      title: {
        display: true,
        text: 'Distance (km)'
      }
    }
  }
}
</script>
