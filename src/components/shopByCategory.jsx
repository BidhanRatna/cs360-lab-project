// import React from "react";
// import "./shopByCategory.css";

// import dressImg from "../assets/shopbycategory/dress.jpg";
// import shoesImg from "../assets/shopbycategory/shoes.jpg";
// import perfumeImg from "../assets/shopbycategory/perfume.jpg";
// import bagsImg from "../assets/shopbycategory/bags.jpg";

// const ShopByCategory = () => {
//   const categories = [
//     { id: 1, name: "Shop by Dress", image: dressImg },
//     { id: 2, name: "Shop by Shoes", image: shoesImg },
//     { id: 3, name: "Shop by Perfumes", image: perfumeImg },
//     { id: 4, name: "Shop by Bags", image: bagsImg },
//   ];

//   return (
//     <div className="shop-by-category">
//      <h1>Shop by Category</h1>
//      <div className="category_collection">
//       {categories.map((category) => (
//          <div key={category.id} className="category-card">
//             <img src={category.image} alt={category.name} />
//             <div className="overlay">
//                <h3>{category.name}</h3>
//             </div>
//          </div>
//          ))}
//      </div>
    
//     </div>
//   );
// };

// export default ShopByCategory;






import React from "react";
import "./shopByCategory.css";

import dressImg from "../assets/shopbycategory/dress.jpg";
import shoesImg from "../assets/shopbycategory/shoes.jpg";
import perfumeImg from "../assets/shopbycategory/perfume.jpg";
import bagsImg from "../assets/shopbycategory/bags.jpg";

const ShopByCategory = () => {
  const categories = [
    { id: 1, name: "Shop Dress", image: dressImg },
    { id: 2, name: "Shop Shoes", image: shoesImg },
    { id: 3, name: "Shop Perfumes", image: perfumeImg },
    { id: 4, name: "Shop Bags", image: bagsImg },
  ];

  return (
    <div className="shop-by-category">
    <div className="line">
      <hr />
    </div>
      <h1>Shop by Category</h1>
      <br/>
      <div className="category_collection">
        {categories.map((category) => (
          <div key={category.id} className="category-card">
            <img src={category.image} alt={category.name} />
            <button className="category-button">{category.name}</button>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ShopByCategory;