import React, { Component } from 'react';
import ProductosService from './ProductosService';

const productosService = new ProductosService();

class ProductosList extends Component {

    constructor(props) {
        super(props);
        this.state = {
            productos: [],
            nextPageURL: ''
        };
        this.nextPage = this.nextPage.bind(this);
        this.handleDelete = this.handleDelete.bind(this);   
}

componentDidMount(){
    var self = this;
    productosService.getProductos().then(function (result) {
        console.log(result);
        self.setState({ productos: result.data, nextPageURL: result.nextlink})
    });
}

handleDelete(e,pk){
    var self = this;
    productosService.deleteProductos({pk : pk}).then(()=>{
        var newArr = self.state.productos.filter(function(obj){
            return obj.pk !== pk;
        });
        self.setState({productos: newArr})
    });
}
nextPage(){
    var self = this;
    console.log(this.state.nextPageURL);
    productosService.getProductosByURL(this.state.nextPageURL).then((result) => {
        self.setState({ productos: result.data, nextPageURL: result.nextlink})
    });
}

render(){
    return(
        <div className="productos--list">
            <table className="table">
            <thead key="thead">
            <tr>
                <th>#</th>
                <th>Codigo</th>
                <th>Nombre</th>
                <th>Categoria</th>
                <th>Estado</th>
                <th>Descripcion</th>
            </tr>
            </thead>
            <tbody>
                {this.state.productos.map( c => 
                   <tr key={c.pk}>
                       <td>{c.pk}</td>
                       <td>{c.codigo}</td>
                       <td>{c.categoria}</td>
                       <td>{c.estado}</td>
                       <td>{c.descripcion}</td>
                       <td>
                           <button onClick={(e) => this.handleDelete(e,c.pk)}>Delete</button>
                           <a href={"/productos/" + c.pk}>Update</a>
                       </td>
                   </tr>
                   )}
            </tbody>
            </table>
            <button className="btn btn-primary" onClick= {this.nextPage}>Next</button>
        </div>
    );
}
}
export default ProductosList;
