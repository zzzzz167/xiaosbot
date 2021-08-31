<template>
  <div v-for="log in logs" :key="log">
      <span>{{log}}</span>
      <el-divider></el-divider>
  </div>
</template>

<script>
export default {
    data(){
        return{
            logn:"hhhh",
            logs: []
        }
    },
    mounted(){
        var ws = new WebSocket('ws://192.168.2.101:6010/ws/logs')
        ws.onmessage = (event) =>{
          ws.send("OK")
          this.logs.push(event.data)
        }
        ws.onclose = () =>{
              this.$notify.info({
                    title: 'Info',
                    message: 'WebSocket连接已断开！请刷新页面',
                    showClose: false
              });
        }
    }
}
</script>

<style>

</style>