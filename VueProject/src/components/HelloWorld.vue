<script lang="ts" >
import { ref } from 'vue'

const activeIndex = ref('1')
const activeIndex2 = ref('1')
const handleSelect = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)}

</script>

<template>

</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
