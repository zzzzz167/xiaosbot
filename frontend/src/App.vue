<template>
<el-row class="tac">
  <el-col :span="3">
    <el-menu>
      <div class="title">
        <i class="el-icon-coffee"></i>
        Avilla dashboard
      </div>
     <el-menu-item index="1">
        <i class="el-icon-setting"></i>
        <template #title>状态</template>
      </el-menu-item>
    </el-menu>
  </el-col>
</el-row>
</template>

<script lang="ts">
  export default{
    data(){
      return{
        message: "hello"
      }
    }
  }
</script>

<style>
.el-icon-coffee{
  color: #8cc269;
}
</style>