


import typing




class AbstractConstraint(object):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def __call__(self, value) -> typing.Union[str,None]:
		raise NotImplementedError()
	#

#




class _ConstraintSequence(AbstractConstraint):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	def __init__(self, sequence:typing.List[AbstractConstraint]) -> None:
		self.__sequence = sequence
	#

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def __call__(self, value) -> typing.Union[str,None]:
		for c in self.__sequence:
			s = c(value)
			if s:
				return s
		return None
	#

#



def _packConstraints(constraints:typing.Tuple[AbstractConstraint]) -> typing.Union[AbstractConstraint,None]:
	assert isinstance(constraints, tuple)

	if len(constraints) == 0:
		return None

	if len(constraints) == 1:
		assert isinstance(constraints[0], AbstractConstraint)
		return constraints[0]

	ret = []
	for c in constraints:
		assert isinstance(c, AbstractConstraint)
		ret.append(c)
	return _ConstraintSequence(ret)
#


