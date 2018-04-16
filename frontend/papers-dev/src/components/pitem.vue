<template>
<div>
  <p>{{ title }} - {{ url }} asdasjdaj</p>
</div>
</template>

<script lang='ts'>
import Vue from 'vue';
export default Vue.extend({
  props: ['title', 'url']
});
</script>
