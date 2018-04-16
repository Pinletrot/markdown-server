<template>
<div>
  <input v-model="url" placeholder="paper link">
  <button v-on:click="submit_paper">submit</button>
</div>
</template>

<script lang='ts'>
import Vue from "vue";
import { translate } from "../translators/index";

export default Vue.extend({
  data: () => {
    return { url: "init" };
  },
  methods: {
    submit_paper: function() {
      console.log(124);
      console.log(this.url);
      const item = translate(this.url);
      item.then(res => {
        console.log(res);
      });
    }
  }
});
</script>
