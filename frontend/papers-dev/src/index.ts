import axios from 'axios';
import Vue from 'vue';
import pbar from './components/pbar.vue';
import pitem from './components/pitem.vue';

const app = new Vue({
  el: '#app',
  data: {
    papers: [{
      title: 'initial',
      url: '',
      uid: 0,
    }],
  },
  components: {
    pbar,
    pitem,
  },
  created() {
    const vm = this;
    axios.get(
      '/papers/get_all',
    ).then((response) => {
      vm.papers = response.data.papers;
    }).catch((error) => {
      // console.log('error @ Vue created: ', error);
    });
  },
});
