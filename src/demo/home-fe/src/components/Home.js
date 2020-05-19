import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
import QueryList from "./QueryList";
import NewQueryModal from "./NewQueryModal";
import ReactDOM from "react-dom";

import axios from "axios";

import { API_URL } from "../constants";

class Home extends Component {
  constructor(props) {
    super(props);
    this.state = {
      home: [],
      queryString: "",
    };

    this.handleInputChange = this.handleInputChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  componentDidMount() {
    this.resetState();
  }

  getQuery = () => {
    axios.get(API_URL).then((res) => this.setState({ home: res.data }));
  };

  resetState = () => {
    this.getQuery();
  };

  handleInputChange(event) {
    console.log(event.target.value);
    this.setState({ queryString: event.target.value });
  }

  handleSubmit(event) {
    console.log(this.state.queryString);
    var callbackQuery = this.state.queryString;
    // Make API call using callbackQuery string
    // Modify HTML element below based on API response

    const element = (
      <div>
        <h1>Hello, world!</h1>
        <h2>You queried the string {callbackQuery}.</h2>
      </div>
    );
    ReactDOM.render(element, document.getElementById("bottomdiv"));
  }

  render() {
    return (
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
        <hr />
        <h1> TYANS STUFF XD </h1>
        <Row>
          <div class="input-group mb-3">
            <input
              type="text"
              class="form-control"
              placeholder="Query"
              aria-label="Recipient's username"
              aria-describedby="basic-addon2"
              onChange={this.handleInputChange}
              value={this.state.queryString}
            />
            <div class="input-group-append">
              <button
                class="btn btn-outline-secondary"
                type="Submit"
                onClick={this.handleSubmit}
              >
                Submit
              </button>
            </div>
          </div>
          <div id="bottomdiv"></div>
        </Row>
      </Container>
    );
  }
}

export default Home;
