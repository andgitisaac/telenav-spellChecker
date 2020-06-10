import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
import QueryList from "./QueryList";
import NewQueryModal from "./NewQueryModal";
import ReactDOM from "react-dom";
import { Link } from 'react-router-dom';

import axios from "axios";

import { API_URL, API_URL_ADD, API_URL_SEARCH} from "../constants";

var callbackQuery

class Home extends Component {
  constructor(props) {
    super(props);
    this.state = {
      home: [],
      queryString: "",
      resultString: "",
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
  };

  splitResponseData(data) {
    var initArray = data.split("]],");
    for(var i = 0; i < initArray.length; i++) {
      initArray[i] = initArray[i].replace(/\[/g, '').replace(/\]/g, '').replace(/\"/g, '')
    }
    return initArray;
  }

  splitUnitData(initArray){
    var newArray = []
    for(var i = 0; i < initArray.length; i++) {
      var splitInitArray = initArray[i].split(",")
      newArray.push(splitInitArray)
    }

    for (var i = 0; i < newArray.length; i++){ 
      if (newArray[i].length < 11) {
        var length = 11 - newArray[i].length
        for (var j = 0; j < length; j++){
          newArray[i].push(" ")
        }
      }
    }
    return newArray;
  }

  createTable(tableData) { 
    if (document.getElementById("1")) {
      document.getElementById("1").remove();
    }

    var table = document.createElement('table');
    table.setAttribute("id", "1");
    table.style.margin = "auto"
    var tableBody = document.createElement('tbody');
        
  
    tableData.forEach(function(rowData) {
      var row = document.createElement('tr');

      rowData.forEach(function(cellData) {
        var cell = document.createElement('td');
        cell.appendChild(document.createTextNode(cellData));
        row.appendChild(cell);
      });
  
      tableBody.appendChild(row);
    });
  
    table.appendChild(tableBody);
    document.body.appendChild(table);
  }
  
  renderTableData(dataArray){
    var column = dataArray.length
    var testArray = this.splitUnitData(dataArray)

    var table = []
    for (var i = 0; i < 11; i++){
      var newArray = []
      for (var j = 0; j < column; j++) {
        newArray.push(testArray[j][i])
      }
      table.push(newArray)
    }
    console.log(testArray)
    console.log(table)

    this.createTable(table)
  }

  async handleSubmit(event) {
    callbackQuery = this.state.queryString;
    axios({method:'post',
          url:API_URL_ADD,
          data: {"query": callbackQuery,},
          headers: {
            'Content-Type': 'application/json',
          }})

    axios({method:'post',
          url:API_URL_SEARCH,
          data: {"query": callbackQuery,},
          headers: {
            'Content-Type': 'application/json',
          }}).then(response => {
            //this.setState({resultString: response.data})
            this.state.resultString = response.data
            console.log(this.splitResponseData(this.state.resultString))
            var address = this.splitResponseData(this.state.resultString)
            this.renderTableData(address)
            // const element = (
            //   // <tr>
            //   //   <td>
            //   //     {this.state.resultString}
              
            //   this.renderTableData(address)
            //   //   </td>
            //   // </tr>
            // );
            // ReactDOM.render(element, document.getElementById("bottomtable"));
          })
  }

  render() {
    return (
      <Container style={{ marginTop: "20px" }}>
        <main>
          <Link to="/database">Go to Database</Link>
        </main>
        {/* <Row>
          <Col>
            <QueryList home={this.state.home} resetState={this.resetState} />
          </Col>
        </Row>
        <Row>
          <Col>
            <NewQueryModal create={true} resetState={this.resetState} />
          </Col>
        </Row> */}
        <hr />
        <h1 style={{textAlign: "center"}}> Please type in your address </h1>
        <Row>
          <div class="input-group mb-3">
            <input
              type="text"
              class="form-control"
              placeholder="address"
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
          
        </Row>
        <div>
          <h1 style={{textAlign: "center"}} id='title'> Address Breakdown</h1>
          <div>{this.handleSubmit}</div>
        </div>
      </Container>
    );
  }
}

export default Home;
