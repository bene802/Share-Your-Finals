import React, { Component } from "react";

class Navbar extends Component {
  render() {
    return (
      <nav className="navbar navbar-light bg-light">
        <h1>Share Your Finals</h1>
        <div className="col-4 d-flex justify-content-end align-items-center">
          <a className="btn btn-sm m-2" href="#">
            Home
          </a>
          <a className="btn btn-sm btn-outline-secondary m-2" href="#">
            Sign in
          </a>
          <a className="btn btn-sm btn-outline-secondary" href="#">
            Sign up
          </a>
        </div>
      </nav>
    );
  }
}
export default Navbar;
