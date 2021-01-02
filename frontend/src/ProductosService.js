import axios from 'axios';
const API_URL = 'http://127.0.0.1:8000';

export default class ProductosService{

    constructor(){}

    getProductos(){
        const url = `${API_URL}/api/productos/`;
        return axios.get(url).then(response => response.data);
    }
    getProductosByURL(link){
        const url = `${API_URL}${link}`;
        return axios.get(url).then(response => response.data);
    }
    getProducto(pk){
        const url = `${API_URL}/api/productosDetail/${pk}`;
        return axios.get(url).then(response => response.data);
    }
    deleteProductos(producto){
        const url = `${API_URL}/api/productosDetail/${producto.pk}`;
        return axios.delete(url);
    }
    createProductos(producto){
        const url = `${API_URL}/api/productos/`;
        return axios.post(url,producto);
    }
    updateProducto(producto){
        const url = `${API_URL}/api/productosDetail/${producto.pk}`;
        return axios.put(url,producto);
    }
    
}