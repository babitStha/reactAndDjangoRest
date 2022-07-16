import React from 'react'
import {Container,Nav, Navbar} from 'react-bootstrap';
import {LinkContainer} from 'react-router-bootstrap'


const Header = () => {
  return (
   
        <header>
            <Navbar bg="dark" variant='dark' expand="lg" collapseOnSelect>
      <Container>
        <LinkContainer to='/'>
        <Navbar.Brand>Saloon Supplies</Navbar.Brand>
        </LinkContainer>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
          <LinkContainer to='/cart'>
            <Nav.Link><i className="fa fa-shopping-cart" aria-hidden="true"></i> Cart</Nav.Link>
        </LinkContainer>
        <LinkContainer to="/login">
            <Nav.Link><i className="fa fa-user" aria-hidden="true"></i> Login</Nav.Link>
        </LinkContainer>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
        </header>
        
  )
}

export default Header