<template>
  <div>
    <Header/>
    <div style="display: flex">
      <!--侧边栏-->

      <!--     主体-->
      <router-view style="flex: 1" />
    </div>
  </div>
</template>

<script>

import Header from "../components/Header.vue";


export default {
  name: "Layout",
  components:{

    Header
  }
}
</script>

<style scoped>

</style>