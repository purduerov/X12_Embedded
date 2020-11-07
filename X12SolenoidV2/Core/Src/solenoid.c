/*
 * solenoid.c
 *
 *  Created on: Nov 7, 2020
 *      Author: Conne
 */

#include "solenoid.h"

#define NUM_SOLENOIDS 6

Solenoid solenoidArray[NUM_SOLENOIDS];

SolenoidErrorCode addSolenoid(int solenoidNumber, GPIO_TypeDef* gpioPort, uint16_t gpioPin)
{
	SolenoidErrorCode errorCode;

	//  Check Parameters
	errorCode = verifySolenoidNumber(solenoidNumber);
	if (errorCode != SOLENOID_SUCCESS)
	{
		return errorCode;
	}
	if (gpioPort == NULL)
	{
		return SOLENOID_INVALID_GPIO_PORT;
	}
	if (!IS_GPIO_PIN(gpioPin))
	{
		return SOLENOID_INVALID_GPIO_PIN;
	}

	solenoidArray[solenoidNumber].port = gpioPort;
	solenoidArray[solenoidNumber].pin = gpioPin;

	return SOLENOID_SUCCESS;
}

SolenoidErrorCode addSolenoids(int numberOfSolenoids, int* solenoidNumber, GPIO_TypeDef** gpioPorts, uint16_t* gpioPins)
{
	SolenoidErrorCode errorCode;

	//  Check parameters
	if (numberOfSolenoids > NUM_SOLENOIDS || numberOfSolenoids < 0)
	{
		return SOLENOID_INVALID_NUMBER_OF_SOLENOIDS;
	}

	for (int i = 0; i < numberOfSolenoids; i++)
	{
		errorCode = addSolenoid(solenoidNumber[i], gpioPorts[i], gpioPins[i]);
		if (errorCode != SOLENOID_SUCCESS)
		{
			return errorCode;
		}
	}

	return SOLENOID_SUCCESS;
}

SolenoidErrorCode verifySolenoidNumber(int solenoidNumber)
{
	if (solenoidNumber >= NUM_SOLENOIDS || solenoidNumber < 0)
	{
		return SOLENOID_INVALID_SOLENOID_NUMBER;
	}
	else
	{
		return SOLENOID_SUCCESS;
	}
}

SolenoidErrorCode configureSolenoid(int solenoidNumber, GPIO_InitTypeDef* gpioInit)
{
	SolenoidErrorCode errorCode;

	//  Check parameter
	errorCode = verifySolenoidNumber(solenoidNumber);
	if (errorCode != SOLENOID_SUCCESS)
	{
		return errorCode;
	}

	//  Set Output of Pin to be Logic LOW
	HAL_GPIO_WritePin(solenoidArray[solenoidNumber].port, solenoidArray[solenoidNumber].pin, GPIO_PIN_RESET);

	//  Override gpioInit->Pin with GPIO Pin of selected solenoid
	gpioInit->Pin = solenoidArray[solenoidNumber].pin;

	//  Initialize GPIO Pin for selected solenoid
	HAL_GPIO_Init(solenoidArray[solenoidNumber].port, gpioInit);

	return SOLENOID_SUCCESS;
}

