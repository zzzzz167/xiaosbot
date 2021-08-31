<template>
<el-col :span="6">
  <div class="gauge" :id="id"></div>
</el-col>
</template>

<script>
import * as echarts from 'echarts'

export default {
 props:["id","name","wsget"],
 data(){
     return{
         data: this.wsget
     }
 },
 mounted(){
     let gauge = echarts.init(document.getElementById(this.id))
      gauge.setOption({
        tooltip: {
          formatter: '{a} <br/>{b} : {c}%'
        },
        series: [{
          name: this.name,
          type: 'gauge',
          progress: {
              show: true
          },
          detail: {
              valueAnimation: true,
              formatter: '{value}'
          },
          data: [{
              value: 10,
              name: this.name
          }]
        }]
      });
      setInterval(() => {
        gauge.setOption({
            series: [{
                data: [{
                    value: this.data[this.id],
                    name: this.name
                }]
            }]
        })
      },2000)

 },
 watch:{
     wsget(newValue){
        this.data = newValue
     }
 }
}
</script>

<style>

</style>