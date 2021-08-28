<template>
<el-row :gutter="20">
  <el-col :span="3">
    <el-affix :offset="10">
    <div class="web-info">
      <i class="el-icon-coffee"></i>
      <span class="web-title">Avilla dashboard</span>
    </div>
    <nav>
      <el-menu router>
        <el-menu-item v-for="(menu,index) in menus" :key="index" :index="menu.router">
          <i :class="menu.icon"></i>
          <template #title>{{menu.title}}</template>
        </el-menu-item>
      </el-menu>
    </nav>
    </el-affix>
  </el-col>
  <el-col :span="21">
    <main>
      <router-view/>
    </main>
  </el-col>
</el-row>
</template>

<script>
  export default {
    data() {
      return {
        menus:[{title: "dashboard", icon: "el-icon-monitor", router: "/"},{title: "Saya Modules", icon: "el-icon-box", router: "/about"}]
      }
    }
  }
</script>


<style lang="scss">
#app {
  font-family: 'Helvetica Neue', Helvetica, 'PingFang SC', 'Hiragino Sans GB','Microsoft YaHei', '微软雅黑', Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.web-info{
  text-align:center;
}
.web-info .el-icon-coffee{
  font-size: 30px;
  color: #f1c4cd;
}
.web-info .web-title{
  font-size: 19px;
}
</style>
