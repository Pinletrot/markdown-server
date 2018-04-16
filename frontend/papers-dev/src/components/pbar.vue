<template>
<div>
  <input v-model="message" placeholder="paper link">
  <button v-on:click="submit_paper">submit</button>
</div>
</template>

<script lang='ts'>
import Vue from 'vue';
export default Vue.extend({
  data: () => {
    return { message: 'init' };
  },
  methods: {
    submit_paper : function() {
      console.log(123);
      console.log(this.message);
    }
  }

});
</script>
