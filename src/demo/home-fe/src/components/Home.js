import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
import QueryList from "./QueryList";
import NewQueryModal from "./NewQueryModal";

import axios from "axios";

import { API_URL } from "../constants";

class Home extends Component {
  state = {
    home: []
  };

  componentDidMount() {
    this.resetState();
  }

  getQuery = () => {
    axios.get(API_URL).then(res => this.setState({ home: res.data }));
  };

  resetState = () => {
    this.getQuery();
  };

  render() {
    return (
      <Container style={{ marginTop: "20px" }}>
        <Row>
          <Col>
            <QueryList
              home={this.state.home}
              resetState={this.resetState}
            />
          </Col>
        </Row>
        <Row>
          <Col>
            <NewQueryModal create={true} resetState={this.resetState} />
          </Col>
        </Row>
      </Container>
    );
  }
}

export default Home;