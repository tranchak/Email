import './App.css';
import {Component} from "react";
class App extends Component{
    constructor(props) {
        super(props);
        this.state={
            all_car:[],
        }
    }
    componentDidMount() {
        fetch('http://127.0.0.1:8000/car/')
            .then(response=>response.json())
            .then(cars=>{
                for(let i of cars) {
                    console.log(
                        i.brand, i.model)}
                this.setState({all_car:cars})
            })
    }
    render(){
        // console.log(this.state.all_car)
        return(
            <div>
                   {this.state.all_car.map((item:T, index:number)=><p key={index}>{item.brand}</p>)}
                </div>
        )
    }
}
export default App;
