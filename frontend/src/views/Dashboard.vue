
<template>
  <el-row>
    <el-col :span="6">
      <div class="gauge" id="cpuuse"></div>
    </el-col>
  </el-row>
  <el-row :gutter="20">
      <el-col :span="12">
        <div class="sysinfo">
          <el-descriptions title="系统信息" column="1" border>
            <el-descriptions-item v-for="sysinfo in sysinfos" :key="sysinfo" :label="sysinfo.index" width="25px">
              {{sysinfo.data}}
            </el-descriptions-item>
          </el-descriptions>
        </div>
      </el-col>
      <el-col :span="12"><div class="grid-content bg-purple"></div></el-col>
  </el-row>
</template>

<script>
import * as echarts from 'echarts'
import { onMounted } from 'vue'
import axios from 'axios'

export default {
  setup() {
    onMounted(() => { // 需要获取到element,所以是onMounted的Hook
      let cpuUse = echarts.init(document.getElementById("cpuuse"));
      // 绘制图表
      cpuUse.setOption({
        tooltip: {
          formatter: '{a} <br/>{b} : {c}%'
        },
        series: [{
          name: 'USED',
          type: 'gauge',
          progress: {
              show: true
          },
          detail: {
              valueAnimation: true,
              formatter: '{value}'
          },
          data: [{
              value: 50,
              name: 'CPU Use'
          }]
        }]
      });
    });
  },
  data(){
    return{
      sysinfos: [{index:"loding",data:"loding...."}],
    }
  },
  mounted(){
    this.$nextTick(function(){
      axios.get("http://192.168.2.101:6010/sys-info")
         .then((res) =>{
           this.sysinfos.shift();
           this.sysinfos =[
             {index: "CPU架构", data: res.data["cpuInfo"]},
             {index: "CPU核数", data: res.data["cpuCores"]},
             {index: "系统平台", data: res.data["platform"]},
             {index: "系统信息", data: res.data["sysInfo"]},
             {index: "内存", data: String(res.data["memorySize"])+"MB"},
             {index: "IP地址", data: res.data["ipHost"]},
             {index: "bot启动时间", data: res.data["startTime"]}
           ];
         });
    })
  }
}
</script>

<style>
.gauge{
  width: 100%;
  height: 50vh;
}
</style>
