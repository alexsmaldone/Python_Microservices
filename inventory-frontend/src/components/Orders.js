import React from "react";

function Orders() {
  return (
    <div className="container">
      <main>
        <div className="py-5 text-center">
          <h2>Checkout Form</h2>
          <p className="lead">Buy your favorite product</p>
        </div>

        <form>
          <div className="row g-3">
            <div className="col-sm-6">
              <label className="form-label">Product</label>
              <input className="form-control" />
            </div>
            <div className="col-sm-6">
              <label className="form-label">Quantity</label>
              <input type="number" className="form-control" />
            </div>
          </div>
          <hr className="my-4" />
          <button className="w-100 btn-primary btn-lg">Buy</button>
        </form>
      </main>
    </div>
  );
}

export default Orders;
