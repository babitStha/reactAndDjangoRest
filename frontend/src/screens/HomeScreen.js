import React, {useState, useEffect} from 'react'
import { Row, Col } from 'react-bootstrap'
import Product from '../components/Product'
import axios from 'axios'


const HomeScreen = () => {
  const [products, setProducts] = useState([])
  useEffect(()=>{
    const fetchdata = async()=>{
      const {data} = await axios.get("/api/products/")
      setProducts(data)
    }
    fetchdata()
  })
  return (
    <div>
        <Row >
            {products.map(product =>{

            return (<Col sm={12} md={6} lg={4} xl={3} key={product._id}>
                <Product product={product}/>
            </Col>)
            })}
        </Row>
    </div>
  )
}

export default HomeScreen