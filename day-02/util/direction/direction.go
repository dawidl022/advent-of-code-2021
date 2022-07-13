package direction

type Direction string

const (
	FORWARD = "forward"
	DOWN    = "down"
	UP      = "up"
)

type Move struct {
	Dir    Direction
	Scalar int
}
