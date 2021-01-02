import React, { Component } from 'react';
import ProductosService from './ProductosService';

const productosService = new ProductosService();

class ProductoCreateUpdate extends Component {
    constructor(props){
        super(props);

        this.handleSubmit = this.handleSubmit.bind(this);
    }

    componentDidMount(){
        const { match: { params } } = this.props;
        if(params && params.pk)
        {
            productosService.getProductos(params.pk).then((c)=>{
                this.refs.codigo.value = c.codigo;
                this.refs.name.value = c.name;
                this.refs.categoria.value = c.categoria;
                this.refs.estado.value = c.estado;
                this.refs.descripcion.value = c.descripcion;
            })
        }
    }
    
    //Crear un producto
    handleCreate(){
        productosService.createProductos(
            {
                "codigo": this.refs.codigo.value,
                "name": this.refs.name.value,
                "categoria": this.refs.categoria.value,
                "estado": this.refs.estado.value,
                "descripcion": this.refs.descripcion.value,
            }
        ).then((result)=> {
            alert("Producto Created!");
        }).catch(()=>{
            alert(' There was an error! Please re-check your form');
        });
    }

    //Actualizar Producto
    handleUpdate(pk){
        productosService.updateProducto(
            {
                "pk": pk,
                "codigo": this.refs.codigo.value,
                "name": this.refs.name.value,
                "categoria": this.refs.categoria.value,
                "estado": this.refs.estado.value,
                "descripcion": this.refs.descripcion.value,
            }
        ).then((result)=>{
            console.log(result);
            alert("Producto updated!");
        }).catch(()=>{
            alert('There was an error! Please re-check your form')
        });
    }

    handleSubmit(event){
        const { match: { params }} = this.props;

        if(params && params.pk){
            this.handleUpdate(params.pk);
        }
        else
        {
            this.handleCreate();
        }

        event.preventDefault();
    }

    render(){
        return(
            <form onSubmit={this.handleSubmit}>
                <div className="form-group">
                    <label>
                        Codigo: 
                    </label>
                    <input className="form-control" type="text" ref='codigo'/>

                    <label>
                        Name: 
                    </label>
                    <input className="form-control" type="text" ref='name'/>

                    <label>
                        Categoria: 
                    </label>
                    <input className="form-control" type="text" ref='categoria'/>

                    <label>
                        Estado: 
                    </label>
                    <input className="form-control" type="text" ref='estado'/>

                    <label>
                        Descripcion: 
                    </label>
                    <textarea className="form-control" ref='descripcion'></textarea>

                    <input className="btn btn-primary" type="submit" value="Submit" />
                </div>
            </form>
        );
    }
}

export default ProductoCreateUpdate;