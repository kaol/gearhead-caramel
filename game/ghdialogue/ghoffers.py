from pbge.dialogue import Offer,Reply,Cue,ContextTag
import context


HELLO = Offer('[HELLO]',context=ContextTag([context.HELLO,]))

ATTACK = Offer('[ATTACK]',context=ContextTag([context.ATTACK,]))

CHALLENGE = Offer('[CHALLENGE]',context=ContextTag([context.CHALLENGE,]))



