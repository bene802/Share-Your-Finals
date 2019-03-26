import React, { Component } from "react";

class Intro extends Component {
  render() {
    return (
      <div className="jumbotron p-3 p-md-5 text-white rounded bg-dark">
        <div className="">
          <h2 className="display-4 font-italic">
            <span className="badge badge-pill badge-primary m-2">20</span>
            thoughts are sharing by
            <span className="badge badge-pill badge-primary m-2">5</span>
            students, Join us!
          </h2>
          <p className="lead my-3">
            How is your finals week? Don't be nervous, share your thoughts with
            us right now!
          </p>
        </div>
      </div>
    );
  }
}
export default Intro;
