import React from "react";
import Wrapper from "./Wrapper";
import { useState } from "react";

function ProductsCreate() {
  const [name, setName] = useState("");
  const [price, setPrice] = useState("");
  const [quantity, setQuantity] = useState("");

  return (
    <Wrapper>
      <form className="mt-3">
        <div className="form-floating pb-3">
          <input
            className="form-control"
            placeholder="Name"
            onChange={(e) => setName(e.target.value)}
          />
          <label>Name</label>
        </div>

        <div className="form-floating pb-3">
          <input
            type="number"
            className="form-control"
            placeholder="Price"
            onChange={(e) => setPrice(e.target.value)}
          />
          <label>Price</label>
        </div>

        <div className="form-floating pb-3">
          <input
            type="number"
            className="form-control"
            placeholder="Quantity"
            onChange={(e) => setQuantity(e.target.value)}
          />
          <label>Quantity</label>
        </div>

        <button className="w-100 btn btn-lg btn-primary" type="submit">
          Submit
        </button>
      </form>
    </Wrapper>
  );
}

export default ProductsCreate;
