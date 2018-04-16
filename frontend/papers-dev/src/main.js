import Vue from 'vue'
import axios from 'axios'

Vue.component('paper-item', {
  props: ['title', 'url'],
  template: '<p>{{ title }} - {{ url }}</p>'
})

new Vue({
  el: '#app',
  data: {
    papers: [{
      title: 'data not loaded from server',
      url: '',
      uid: 0
    }],
  },
  created: function () {
    var vm = this;
    console.log('asdad');
    axios.get(
      '/papers/get_all'
    ).then(function (response) {
      vm.papers = response.data['papers'];
    }).catch(function (error) {
      console.log('error @ Vue created: ', error);
    })
  }
});