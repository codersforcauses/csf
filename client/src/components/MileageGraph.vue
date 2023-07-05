<template>
  <v-card variant="flat">
    <v-card-title>Mileage Graph</v-card-title>
    <VCardActions class="d-flex justify-space-between">
      <v-btn v-for="option in ['This Week', 'This Month', 'This Year', 'Overall']" rounded="xl" size="small"> {{ option }} </v-btn>
    </VCardActions>
    <Bar :data="chartData" /> 
  </v-card>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'


ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale);

const props = defineProps({
  labels: {
    type: Array,
    required: true
  },
  datasets: {
    type: Array,
    required: true
  }
})

const chartData = {
        labels: props.labels,
        datasets: props.datasets}
</script>

<!-- The following is what was initially in dashboard view (filtered to include only the relevant information)-->

<!-- 
<template>
  <v-row class="ma-0" align="center">
        <v-col>
          <mileage-graph :labels="tempLabels" :datasets="tempDatasets"/>
        </v-col>
    </v-row>
</template>

<script setup lang="ts">
    import { ref } from "vue"
    import mileageGraph from "@/components/MileageGraph.vue";

    const tempLabels = ref(["January", "February", "March", "April", "May", "June", "July"])
    const tempDatasets = ref([
        {
            label: 'Yearly Mileage',
            backgroundColor: '#f87979',
            data: [40, 39, 10, 40, 39, 80, 40]
        }
    ])
</script> 
-->