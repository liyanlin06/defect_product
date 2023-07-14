<template>


  <div id="Header" >
    <div class="top-left-edition">

    </div>


<div class="menu-con">
  <el-menu class="menu">

    <el-menu-item index="4" class="el-menu" @click="$router.push('/single')">单图片检测</el-menu-item>
    <el-menu-item index="4" class="el-menu" @click="$router.push('/mul')">多图片检测</el-menu-item>

  </el-menu>

</div>








  </div>

</template>

<script>
export default {
  name: "Header"
}

</script>

<style scoped>
#Header {
  //padding: 30px 110px 0 350px;
  display: flex;
  justify-content: center; /* 居中水平对齐 */
  align-items: center; /* 居中垂直对齐 */
  padding: 20px;

  //margin: 10px auto;
}

#word {
  margin-left: 45%;
  margin-top: -35px;
  margin-bottom: 37px;
  height: 60px;
  line-height: 3.2em;
  letter-spacing: 8px;
}

h1 {
  /*text-align: center;*/
  color: #21b3b9;
  letter-spacing: 30px;
  font-size: 2.3em;
}



.top-left-edition span i {
  float: left;
  margin-right: 10px;
}

i,
input,
label {
  vertical-align: middle;
}

i {
  border: 0;
  display: block;
  cursor: pointer;
}

.top-left-edition span {
  float: left;
  font-size: 16px;
  color: #999999;
  line-height: 24px;
  margin-right: 40px;
}

.menu {
  display: flex;
}
.el-menu{
  flex: 1;
}
</style>