import React from "react";
import { Button, Form, FormGroup, Input, Label } from "reactstrap";

import axios from "axios";

import { API_URL, API_URL_ADD } from "../constants";

class NewQueryForm extends React.Component {
  state = {
      pk:0,
      query: ""
  };

  componentDidMount() {
    if (this.props.homes) {
      const { pk, query } = this.props.homes;
      this.setState({ pk, query });
    }
  }

  onChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  };

  createQuery = e => {
    e.preventDefault();
    axios.post(API_URL_ADD, this.state).then(() => {
      this.props.resetState();
      this.props.toggle();
    });
  };


  editQuery = e => {
    e.preventDefault();
    axios.put(API_URL_ADD + this.state.pk, this.state).then(() => {
      this.props.resetState();
      this.props.toggle();
    });
  };


  defaultIfEmpty = value => {
    return value === "" ? "" : value;
  };

  render() {
    return (
      <Form onSubmit={this.props.homes ? this.editQuery : this.createQuery}>
        <FormGroup>
          <Label for="query">query:</Label>
          <Input
            type="json"
            name="query"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.query)}
          />
        </FormGroup>
        <Button>Send</Button>
      </Form>
    );
  }
}

export default NewQueryForm;