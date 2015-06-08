import React from 'react'

import CartItemDescription from './CartItemDescription.js'
import CartItemCount from './CartItemCount.js'
import CartItemTotal from './CartItemTotal.js'


let CartItem = React.createClass({
    propTypes: {
        item: React.PropTypes.shape({
            id: React.PropTypes.any.isRequired,
            count: React.PropTypes.number,
            value: React.PropTypes.number,
            desc: React.PropTypes.string
        }),
        inc: React.PropTypes.func.isRequired,
        dec: React.PropTypes.func.isRequired
    },
    getDefaultProps () {
        return {
            item: {
                count: 0,
                value: 0,
                desc: ''
            }
        };
    },
    render () {
        return (<div>
                    <CartItemDescription ref="itemDesc" desc={this.props.item.desc}/>
                    <CartItemCount ref="itemCount" count={this.props.item.count} itemId={this.props.item.id} inc={this.props.inc} dec={this.props.dec}/>
                    <CartItemTotal ref="itemTotal" value={this.props.item.value} count={this.props.item.count}/>
                </div>);
    }
});

export default CartItem;
