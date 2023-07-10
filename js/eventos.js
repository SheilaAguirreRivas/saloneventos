const { createApp } = Vue;

createApp({
  data() {
    return {
      eventos: [],
      url: 'http://127.0.0.1:5000/eventos',
      //'http://127.0.0.1:5000/eventos',
      //'http://sheiaguirrer.pythonanywhere.com/eventos',
      cargando: true,
      error: false
    };
  },

  methods: {
    fetchData(url) {
      fetch(url)
        .then(response => response.json())
        .then(data => {
          this.eventos = data;
          this.cargando = false;
        })
        .catch(err => {
          console.error(err);
          this.error = true;
        });
    },

    eliminar(evento) {
      const url = this.url+'/'+evento;
      let options = {
        method: 'DELETE'
      };
      fetch(url, options)
        .then(res => res.json())
        .then(res => {
          location.reload();
        })
        .catch(err => {
          console.error(err);
          this.error = true;
        });
      }
    },
    

  created() {
    this.fetchData(this.url);
  }
}).mount('#app');
