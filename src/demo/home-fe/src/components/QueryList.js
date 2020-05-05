import React, { Component } from "react";
import { Table } from "reactstrap";
import NewQueryModal from "./NewQueryModal";

import ConfirmRemovalModal from "./ConfirmRemovalModal";

class QueryList extends Component {
  render() {
    const home = this.props.home;
    return (
      <Table dark>
        <thead>
          <tr>
            <th>query</th>
            <th>query_date</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {!home || home.length <= 0 ? (
            <tr>
              <td colSpan="6" align="center">
                <b>Ops, no one here yet</b>
              </td>
            </tr>
          ) : (
            home.map(homes => (
              <tr key={homes.pk}>
                <td>{homes.query}</td>
                <td>{homes.query_date}</td>
                <td align="center">
                  <NewQueryModal
                    create={false}
                    homes={homes}
                    resetState={this.props.resetState}
                  />
                  &nbsp;&nbsp;
                  <ConfirmRemovalModal
                    pk={homes.pk}
                    resetState={this.props.resetState}
                  />
                </td>
              </tr>
            ))
          )}
        </tbody>
      </Table>
    );
  }
}

export default QueryList;