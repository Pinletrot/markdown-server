<template>
  <p>{{ title }} - {{ url }}</p>
</template>

<script>
import Vue from "vue";
export default Vue.extend({
  props: ["title", "url"]
});
</script>
