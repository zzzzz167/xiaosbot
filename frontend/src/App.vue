<template>
  <el-row :gutter="20">
    <el-col :span="3">
      <Menu></Menu>
    </el-col>
    <el-col :span="20">
      
    </el-col>
  </el-row>
</template>

<script>
import Menu from './components/menu.vue'
export default{
  components:{
    Menu
  }
}

</script>

<style>
.body{
  font-family: 'Helvetica Neue', Helvetica, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', '微软雅黑', Arial, sans-serif;
}
</style>