<template>
  <div v-if="!loading">
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
</div>
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
import { ref, computed, onMounted } from 'vue'
import type Mileage from '../types/mileage'
import { useMileageStore } from '@/stores/mileage'

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend) // creating instance of chart

// DATA FILTERING AND COMPUTED PROPERTIES
const tempData = ref<Mileage[]>([
  { mileageId: 1, user: 1, kilometres: 10, date: '2023-06-01' },
  { mileageId: 2, user: 1, kilometres: 20, date: '2023-06-02' },
  { mileageId: 3, user: 1, kilometres: 50, date: '2023-06-03' },
  { mileageId: 4, user: 1, kilometres: 60, date: '2023-06-04' },
  { mileageId: 5, user: 1, kilometres: 30, date: '2023-06-05' },
  { mileageId: 6, user: 1, kilometres: 40, date: '2023-06-06' },
  { mileageId: 7, user: 1, kilometres: 10, date: '2023-06-07' },
  { mileageId: 8, user: 1, kilometres: 2, date: '2023-06-08' },
  { mileageId: 9, user: 1, kilometres: 10, date: '2023-06-09' },
  { mileageId: 10, user: 1, kilometres: 20, date: '2023-06-10' },
  { mileageId: 11, user: 1, kilometres: 30, date: '2023-06-11' },
  { mileageId: 12, user: 1, kilometres: 54, date: '2023-06-12' },
  { mileageId: 13, user: 1, kilometres: 12, date: '2023-06-13' },
  { mileageId: 14, user: 1, kilometres: 31, date: '2023-06-14' },
  { mileageId: 15, user: 1, kilometres: 30, date: '2023-06-15' },
  { mileageId: 16, user: 1, kilometres: 10, date: '2023-06-16' },
  { mileageId: 17, user: 1, kilometres: 70, date: '2023-06-17' },
  { mileageId: 18, user: 1, kilometres: 10, date: '2023-06-18' },
  { mileageId: 19, user: 1, kilometres: 5, date: '2023-06-19' },
  { mileageId: 20, user: 1, kilometres: 10, date: '2023-06-20' },
  { mileageId: 21, user: 1, kilometres: 20, date: '2023-06-21' },
  { mileageId: 22, user: 1, kilometres: 32, date: '2023-06-22' },
  { mileageId: 23, user: 1, kilometres: 10, date: '2023-06-23' },
  { mileageId: 24, user: 1, kilometres: 5, date: '2023-06-24' },
  { mileageId: 25, user: 1, kilometres: 15, date: '2023-06-25' },
  { mileageId: 26, user: 1, kilometres: 10, date: '2023-06-26' },
  { mileageId: 27, user: 1, kilometres: 20, date: '2023-06-27' },
  { mileageId: 28, user: 1, kilometres: 30, date: '2023-06-28' },
  { mileageId: 29, user: 1, kilometres: 20, date: '2023-06-29' },
  { mileageId: 30, user: 1, kilometres: 50, date: '2023-06-30' },
  { mileageId: 31, user: 1, kilometres: 60, date: '2023-07-01' },
  { mileageId: 32, user: 1, kilometres: 50, date: '2023-07-02' },
  { mileageId: 33, user: 1, kilometres: 80, date: '2023-07-03' },
  { mileageId: 34, user: 1, kilometres: 30, date: '2023-07-04' },
  { mileageId: 35, user: 1, kilometres: 10, date: '2023-07-05' },
  { mileageId: 36, user: 1, kilometres: 14, date: '2023-07-06' },
  { mileageId: 37, user: 1, kilometres: 20, date: '2023-07-07' },
  { mileageId: 38, user: 1, kilometres: 13, date: '2023-07-08' }
])

const mileageStore = useMileageStore()
const dataPoints = ref()
const loading = ref(true)
const filteredData = ref<Mileage[]>()
const labels = computed(() => filteredData.value?.map((data) => data.date))
const data = computed(() => filteredData.value?.map((data) => data.kilometres))
const activeButton = ref('This Week')

function updateData() {
  mileageStore.getMileageDataPointsByTeam()
  dataPoints.value = mileageStore.dataPoints
}
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
    minDate = dataPoints.value.reduce((min, obj) => {
      const currentDate = new Date(obj.date)
      return currentDate < min ? currentDate : min
    }, new Date())
  }

  filteredData.value = []
  while (currentDate >= minDate) {
    const dateString = currentDate.toISOString().split('T')[0]
    // changing labels based on the range selected
    let datalabel = ''

    const daysOfWeek = ['Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri']
    const monthsOfYear = [
      'Jan',
      'Feb',
      'Mar',
      'Apr',
      'May',
      'Jun',
      'Jul',
      'Aug',
      'Sept',
      'Oct',
      'Nov',
      'Dec'
    ]

    const day = currentDate.getDate()
    const weekday = daysOfWeek[currentDate.getDay()]
    const month = monthsOfYear[currentDate.getMonth()]
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
    const matchingData = dataPoints.value.find((obj) => obj.date === dateString)
    filteredData.value?.unshift({
      mileageId: matchingData ? matchingData.mileageId : -1,
      user: matchingData ? matchingData.user : -1,
      kilometres: matchingData ? matchingData.kilometres : 0,
      date: datalabel ? datalabel : dateString
    })
    currentDate.setDate(currentDate.getDate() - 1)
  }
}


updateData()
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
