<template>
<div>
  <a-rate v-model="value" />
  <el-calendar v-model="dates"></el-calendar>
</div>
</template>
<script>
export default {
  data() {
    return {
      value: 2,
      dates:new Date()
    };
  },
};
</script>
