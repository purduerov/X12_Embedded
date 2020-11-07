/*
 * solenoid.h
 *
 *  Created on: Nov 7, 2020
 *      Author: Conne
 */

#ifndef INC_SOLENOID_H_
#define INC_SOLENOID_H_

#include "stm32f0xx_hal.h"

//  Solenoid Error Codes
typedef enum SolenoidErrorCodeEnum
{
	SOLENOID_SUCCESS = 0,
	SOLENOID_INVALID_SOLENOID_NUMBER = 1,
	SOLENOID_INVALID_GPIO_PORT = 2,
	SOLENOID_INVALID_GPIO_PIN = 3,
	SOLENOID_INVALID_NUMBER_OF_SOLENOIDS = 4
} SolenoidErrorCode;

typedef struct SolenoidStruct
{
	GPIO_TypeDef* port;
	uint16_t pin;
} Solenoid;

//  Function Declarations
SolenoidErrorCode verifySolenoidNumber(int solenoidNumber);

SolenoidErrorCode addSolenoid(int solenoidNumber, GPIO_TypeDef* gpioPort, uint16_t gpioPin);
SolenoidErrorCode addSolenoids(int numberOfSolenoids, int* solenoidNumber, GPIO_TypeDef** gpioPorts, uint16_t* gpioPins);
SolenoidErrorCode configureSolenoid(int solenoidNumber, GPIO_InitTypeDef* gpioInit);


#endif /* INC_SOLENOID_H_ */
