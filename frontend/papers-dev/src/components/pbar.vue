<template>
<div>
  <input v-model="url" placeholder="paper link">
  <button v-on:click="submit_paper">submit</button>
</div>
</template>

<script lang='ts'>
import axios from "axios";
import Vue from "vue";
import { translate } from "../translators/index";

export default Vue.extend({
  data: () => {
    return { url: "https://arxiv.org/abs/1804.03228" };
  },
  methods: {
    submit_paper: function() {
      const proxy_prefix = "/papers/fetch?url=";
      const proxied_url = proxy_prefix + this.url;

      translate(proxied_url).then(paperItem => {
        paperItem.url = paperItem.url.replace(proxy_prefix, "");
        axios.post("/papers/add", paperItem).then(res_post => {
          console.log(res_post);
        });
      });
    }
  }
});
</script>
