const productos = [
    {
      url:
        "https://sodimac.scene7.com/is/image/SodimacCL/8758581?fmt=jpg&fit=fit,1&wid=160&hei=160",
      descripcion: "una cama"
    },
    {
      url:
        "https://sodimac.scene7.com/is/image/SodimacCL/358930?fmt=jpg&fit=fit,1&wid=160&hei=160",
      descripcion: "una casa de perro"
    },
    {
      url:
        "https://sodimac.scene7.com/is/image/SodimacCL/8796408?fmt=jpg&fit=fit,1&wid=160&hei=160",
      descripcion: "una cama pero de perro"
    },
        {
        url:
            "https://sodimac.scene7.com/is/image/SodimacCL/367584X?fmt=jpg&fit=fit,1&wid=160&hei=160",
        descripcion: "un collar"
        }
]


var texto_iterable=""

productos.forEach((element) => {

    var tarjetita_html = `<div class="col">
    <div class="card" style="width: 18rem;">
        <img src="${element.url}" class="card-img-top" alt="foto">
        <div class="card-body">
          <h5 class="card-title">Card title</h5>
          <p class="card-text">${element.descripcion}</p>
          <a href="#" class="btn btn-primary">Go somewhere</a>
        </div>
      </div>
    </div>`
    
    texto_iterable += tarjetita_html
    $("#productos").html( texto_iterable )
});

  