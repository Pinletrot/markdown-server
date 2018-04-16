import Vue from 'vue'
import axios from 'axios'
import pitem from './components/pitem.vue'


new Vue({
  el: '#app',
  data: {
    papers: [{
      title: 'initial',
      url: '',
      uid: 0
    }],
  },
  components: {
    pitem
  },
  created: function () {
    var vm = this;
    axios.get(
      '/papers/get_all'
    ).then(function (response) {
      vm.papers = response.data['papers'];
    }).catch(function (error) {
      console.log('error @ Vue created: ', error);
    })
  }
});