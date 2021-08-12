import { React, useState } from 'react'
import { FaStar } from 'react-icons/fa'

const StarRating = ( { totalStars = 5 }) => {

    const Star = ({ selected = false, onSelect = f => f }) => (
        <FaStar color={selected ? "red" : "gray"} onClick={onSelect} />
    )

    const [selectedStars, setSelectedStars] = useState(0)

    return (
        <>
            {[...Array(totalStars)].map((n, i) => (
                <Star
                 key={i}
                 selected={selectedStars > i}
                 onSelect={() => setSelectedStars(i + 1)}
                 /> ))}
            <p>
                {selectedStars} of {totalStars} stars.
            </p>
        </>
    )
}

export default StarRating   