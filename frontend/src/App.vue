<template>
<el-row :gutter="20">
  <el-col :span="4">
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
  <el-col :span="20">
    <main>
      <el-affix :offset="0">
        <div class="main-nav">
          <p class="page-title">{{$route.name}}</p>
        </div>
      </el-affix>
      <div>
        <router-view/>
      </div>
    </main>
  </el-col>
</el-row>
</template>

<script>
  export default {
    data() {
      return {
        menus:[{title: "Dashboard", icon: "el-icon-monitor", router: "/"},
        {title: "Saya Modules", icon: "el-icon-box", router: "/modules"},
        {title: "Log Output", icon:"el-icon-notebook-2", router: "/log"}]
      }
    }
  }
</script>


<style lang="scss">
#app {
  font-family: 'Helvetica Neue', Helvetica, 'PingFang SC', 'Hiragino Sans GB','Microsoft YaHei', '微软雅黑', Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin: -8px -8px auto;
}
nav{
  text-align: center;
  font-size: 13px;
  height: 100%;
}
.web-info{
  text-align:center;
}
.web-info .el-icon-coffee{
  font-size: 30px;
  color: #f1c4cd;
}
.web-info .web-title{
  font-size: 25px;
  font-weight: bold;
}
.page-title{
  font-size: 20px;
}
.main-nav{
   z-index: 3;
   margin-top: 0px;
   padding: 3px;
   background-color: #FFFFFF;
   border-radius: 20px;
}
</style>
