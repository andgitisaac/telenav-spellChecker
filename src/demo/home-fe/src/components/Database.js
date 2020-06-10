import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
import QueryList from "./QueryList";
import NewQueryModal from "./NewQueryModal";
import ReactDOM from "react-dom";
import { Link } from 'react-router-dom';
import Header from "./Header";
import axios from "axios";

import { API_URL, API_URL_ADD, API_URL_SEARCH} from "../constants";

class Database extends Component {
  constructor(props) {
    super(props);
    this.state = {
      home: [],
    };
  }

  componentDidMount() {
    this.resetState();
  }

  getQuery = () => {
    axios.get(API_URL).then((res) => this.setState({ home: res.data }));
  };

  resetState = () => {
    this.getQuery();
    if (document.getElementById("1")) {
        document.getElementById("1").remove();
    }
  };
  

  render() {
    return (
      <>
      <Header />
      <Container style={{ marginTop: "20px" }}>
        <Row>
          <Col>
            <QueryList home={this.state.home} resetState={this.resetState} />
          </Col>
        </Row>
        <Row>
          <Col>
            <NewQueryModal create={true} resetState={this.resetState} />
          </Col>
        </Row>
      </Container>
      </>
    );
  }
}

export default Database;
