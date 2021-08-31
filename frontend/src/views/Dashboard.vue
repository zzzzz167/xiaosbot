
<template>
  <el-row>
      <Gauge v-for="gauge in gauges" 
               :key="gauge.id" 
               :id="gauge.id" 
               :name="gauge.name"
               :wsget="wsget">
      </Gauge>
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
      <el-col :span="12">
        <el-descriptions title="Avilla Info" column="1" border>
          <el-descriptions-item v-for="sayainfo in sayainfos" :key="sayainfo" :label="sayainfo.index" width="25px">
              {{sayainfo.data}}
            </el-descriptions-item>
        </el-descriptions>
      </el-col>
  </el-row>
</template>

<script>
import axios from 'axios'
import Gauge from '../components/gauge.vue'

export default {
  components:{
    Gauge
  },
  data(){
    return{
      wsget: [],
      sysinfos: [{index: "loading", data: "loading...."}],
      sayainfos: [{index: "loading", data: "loading...."}],
      gauges: [{id: "cpuUse", name:"CPU占用率"},
               {id: "cpuTem", name:"CPU温度"},
               {id: "vMemUse", name:"物理内存使用"},
               {id: "sMemUse", name:"虚拟内存使用"}]
    }
  },
  mounted(){

    this.$nextTick(function(){
      axios.get("http://192.168.2.101:6010/sys-info")
         .then((res) =>{
           this.sysinfos.shift();
           this.sayainfos.shift();
           this.sysinfos =[
             {index: "CPU架构", data: res.data["cpuInfo"]},
             {index: "CPU核数", data: res.data["cpuCores"]},
             {index: "系统平台", data: res.data["platform"]},
             {index: "系统信息", data: res.data["sysInfo"]},
             {index: "内存", data: String(res.data["memorySize"])+"MB"},
             {index: "IP地址", data: res.data["ipHost"]},
             {index: "bot启动时间", data: res.data["startTime"]}
           ];
           this.sayainfos=[
             {index: "python版本", data: res.data["pythonVersion"]},
             {index: "Avilla版本", data: res.data["avillaVersion"]},
             {index: "Saya Modules", data: res.data["Plugins"]},
             {index: "网络收包", data: res.data["NetRecv"]},
             {index: "网络发包", data: res.data["net_sent"]}
           ]
         });
      var ws = new WebSocket('ws://192.168.2.101:6010/ws/sys-status')
        ws.onmessage = (event) =>{
          this.wsget = JSON.parse(event.data)
        }
        ws.onclose = () =>{
          this.$notify.info({
                    title: 'Info',
                    message: 'WebSocket连接已断开！请刷新页面',
                    showClose: false
          });
        }
    });
  }
}
</script>

<style>
.gauge{
  width: 100%;
  height: 50vh;
}
</style>
