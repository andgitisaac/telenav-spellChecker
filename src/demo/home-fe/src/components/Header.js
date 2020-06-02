import React, { Component } from "react";

class Header extends Component {
  render() {
    return (
      <div className="text-center">
        <img
          src="https://images.acvmagazine.com/file/BIT-Magazine-Images/0908-1.jpg"
          width="300"
          className="img-thumbnail"
          style={{ marginTop: "20px" }}
        />
      </div>
    );
  }
}

export default Header;