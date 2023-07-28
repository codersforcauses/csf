import { createTypedChart } from 'vue-chartjs'
import { LineController } from 'chart.js'

class LineWithLineController extends LineController {
  static override id = 'line-with-line'

  public override draw() {
    super.draw()
  }
}

const LineWithLineChart = createTypedChart('line-with-line' as 'line', LineWithLineController)

export default LineWithLineChart
