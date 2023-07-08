<template>
  <v-card variant="flat">
    <v-card-title>Mileage Graph</v-card-title>
    <v-card-actions class="d-flex justify-space-between">
      <v-btn
        class="text-secondaryGreen"
        variant="tonal"
        v-for="option in ['This Week', 'This Month', 'This Year', 'Overall']"
        :key="option"
        rounded="xl"
        size="small"
      >
        {{ option }}
      </v-btn>
    </v-card-actions>
    <LineWithLineChart :data="data" :options="options" />
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
  Legend,
} from 'chart.js'
import type { ChartDataset } from 'chart.js'
import LineWithLineChart from '../types/LineWithLineChart'

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend)

const DATA_COUNT = 12
const labels = []
for (let i = 0; i < DATA_COUNT; ++i) {
  labels.push(i.toString())
}
const datapoints = [0, 20, 20, 60, 60, 120, 180, 120, 125, 105, 110, 170]
const data = {
  labels: labels,
  datasets: [
    {
      label: 'KMs run over time',
      data: datapoints,
      borderColor: 'rgb(255, 99, 99)',
      fill: false,
      cubicInterpolationMode: 'monotone',
      tension: 0.4
    } as ChartDataset<'line', (number | null)[]> // Update the type assertion
  ]
};

const options = {
  plugins: {
    legend: {
      display: false,
    }
  },
  responsive: true,
  maintainAspectRatio: true,
  tooltips: {
    intersect: false
  }
}
</script>
