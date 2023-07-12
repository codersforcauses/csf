<template>
  <v-card variant="flat" class="chart-container">
    <v-card-actions class="d-flex justify-space-between">
      <v-btn
        class="text-secondaryGreen"
        variant="tonal"
        v-for="duration in ['This Week', 'This Month', 'This Year', 'Overall']"
        :key="duration"
        rounded="xl"
        size="small"
        @click="filterData(duration)"
      >
        {{ duration }}
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

const tempData = [
  { mileage_id: 1, user_id: 1, kilometers: 10, date: '2023-06-01' },
  { mileage_id: 2, user_id: 1, kilometers: 20, date: '2023-06-02' },
  { mileage_id: 3, user_id: 1, kilometers: 50, date: '2023-06-03' },
  { mileage_id: 4, user_id: 1, kilometers: 60, date: '2023-06-04' },
  { mileage_id: 5, user_id: 1, kilometers: 30, date: '2023-06-05' },
  { mileage_id: 6, user_id: 1, kilometers: 40, date: '2023-06-06' },
  { mileage_id: 7, user_id: 1, kilometers: 10, date: '2023-06-07' },
  { mileage_id: 8, user_id: 1, kilometers: 2, date: '2023-06-08' },
  { mileage_id: 9, user_id: 1, kilometers: 10, date: '2023-06-09' },
  { mileage_id: 10, user_id: 1, kilometers: 20, date: '2023-06-10' },
  { mileage_id: 11, user_id: 1, kilometers: 30, date: '2023-06-11' },
  { mileage_id: 12, user_id: 1, kilometers: 54, date: '2023-06-12' },
  { mileage_id: 13, user_id: 1, kilometers: 12, date: '2023-06-13' },
  { mileage_id: 14, user_id: 1, kilometers: 31, date: '2023-06-14' },
  { mileage_id: 15, user_id: 1, kilometers: 30, date: '2023-06-15' },
  { mileage_id: 16, user_id: 1, kilometers: 10, date: '2023-06-16' },
  { mileage_id: 17, user_id: 1, kilometers: 70, date: '2023-06-17' },
  { mileage_id: 18, user_id: 1, kilometers: 10, date: '2023-06-18' },
  { mileage_id: 19, user_id: 1, kilometers: 5, date: '2023-06-19' },
  { mileage_id: 20, user_id: 1, kilometers: 10, date: '2023-06-20' },
  { mileage_id: 21, user_id: 1, kilometers: 20, date: '2023-06-21' },
  { mileage_id: 22, user_id: 1, kilometers: 32, date: '2023-06-22' },
  { mileage_id: 23, user_id: 1, kilometers: 10, date: '2023-06-23' },
  { mileage_id: 24, user_id: 1, kilometers: 5, date: '2023-06-24' },
  { mileage_id: 25, user_id: 1, kilometers: 15, date: '2023-06-25' },
  { mileage_id: 26, user_id: 1, kilometers: 10, date: '2023-06-26' },
  { mileage_id: 27, user_id: 1, kilometers: 20, date: '2023-06-27' },
  { mileage_id: 28, user_id: 1, kilometers: 30, date: '2023-06-28' },
  { mileage_id: 29, user_id: 1, kilometers: 40, date: '2023-06-29' },
  { mileage_id: 30, user_id: 1, kilometers: 50, date: '2023-06-30' },
  { mileage_id: 31, user_id: 1, kilometers: 60, date: '2023-07-01' },
  { mileage_id: 32, user_id: 1, kilometers: 70, date: '2023-07-02' },
  { mileage_id: 33, user_id: 1, kilometers: 80, date: '2023-07-03' },
  { mileage_id: 34, user_id: 1, kilometers: 90, date: '2023-07-04' },
  { mileage_id: 35, user_id: 1, kilometers: 100, date: '2023-07-05' },
  { mileage_id: 36, user_id: 1, kilometers: 110, date: '2023-07-06' },
  { mileage_id: 37, user_id: 1, kilometers: 120, date: '2023-07-07' },
  { mileage_id: 38, user_id: 1, kilometers: 130, date: '2023-07-08' }
]

const filteredData = ref<Mileage[]>()

const filterData = (duration: string) => {
  let minDate = new Date()

  if (duration === 'This Week') minDate.setDate(minDate.getDate() - 7)
  if (duration === 'This Month') minDate.setDate(minDate.getDate() - 30)
  if (duration === 'This Year') minDate.setDate(minDate.getDate() - 365)
  if (duration === 'Overall') minDate.setDate(minDate.getDate() - 3650) // change this

  filteredData.value = tempData.filter((data) => data.date >= minDate.toISOString().split('T')[0])
}

filterData('This Week')

const graphData = computed(() => {
  return {
    labels: filteredData.value?.map((data) => data.date),
    datasets: [
      {
        data: filteredData.value?.map((data) => data.kilometers),
        borderColor: 'rgb(255, 99, 99)',
        fill: false,
        cubicInterpolationMode: 'monotone',
        tension: 0.4
      } as ChartDataset<'line', (number | null)[]> // Update the type assertion
    ]
  }
})

const options = {
  plugins: {
    legend: {
      display: false
    }
  },
  responsive: true,
  maintainAspectRatio: true,
  tooltips: {
    intersect: false
  }
}
</script>
