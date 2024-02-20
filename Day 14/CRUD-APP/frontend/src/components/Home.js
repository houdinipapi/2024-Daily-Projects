import student1 from "../static/img/student1.jpg";
import student2 from "../static/img/student2.jpg"; 
import student3 from "../static/img/student3.jpg";

import Carousel from 'react-bootstrap/Carousel';

const Home = () => {
    return (
        <div className="row">
            <Carousel data-bs-theme="dark">

                <Carousel.Item>
                    <img
                        className="d-block w-100"
                        src={student1}
                        alt="First slide"
                    />
                </Carousel.Item>

                <Carousel.Item>
                    <img
                        className="d-block w-100"
                        src={student2}
                        alt="Second slide"
                    />
                </Carousel.Item>

                <Carousel.Item>
                    <img
                        className="d-block w-100"
                        src={student3}
                        alt="Third slide"
                    />
                </Carousel.Item>

            </Carousel>
        </div>
        
    );
}

export default Home;