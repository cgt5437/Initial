package fraction;
/*
 * Created by Christian Thomas
 */

public class Fraction {
	
	    public int numerator;
	    public int denominator;
	    
	    public Fraction()
	    {
	        numerator = 1;
	        denominator = 1;
	    }
	    public Fraction(int numer, int denom)
	    {
	        numerator = numer;
	        denominator = denom;
	        if (denominator == 0)
	        {
	            System.out.println("Divide by zero error -- setting value to 0");
	            denominator = 1;
	            numerator = 0;
	        }
	            
	    }
	    public Fraction(int numer)
	    {
	        numerator = numer;
	        denominator = 1;
	    }
	    public Fraction(Fraction second)
	    {
	        numerator = second.numerator;
	        denominator = second.denominator;
	    }
	    public boolean equals(Fraction secondFraction)
	    {
	        return (numerator == secondFraction.numerator && denominator == secondFraction.denominator);
	    }
	    public boolean LessThan (Fraction secondFraction)
	    {
	    	/**
	    	 * Have to turn numerator and denominator into doubles
	    	 */
	        double n = numerator;
	        double d = denominator;
	        double a = n / d;
	        double secondN = secondFraction.numerator;
	        double secondD = secondFraction.denominator;
	        double b = secondN / secondD;
	        return a < b;
	    }
	    public Fraction add(Fraction secondFraction)
	    {
	       Fraction result = new Fraction((numerator * secondFraction.denominator) + (denominator
	       * secondFraction.numerator), denominator * secondFraction.denominator);
	       result.reduce();
	       return result;
	    }
	    public Fraction subtract(Fraction secondFraction)
	    {
	        Fraction result = new Fraction((numerator * secondFraction.denominator) - (denominator
	       * secondFraction.numerator), denominator * secondFraction.denominator);
	       result.reduce();
	       return result;
	    }
	    public Fraction multiply (Fraction secondFraction)
	    {
	        Fraction result = new Fraction(numerator * secondFraction.numerator,
	        denominator * secondFraction.denominator);
	        result.reduce();
	        return result;
	        
	    }
	    public Fraction  divide (Fraction secondFraction)
	    {
	        Fraction result = new Fraction(numerator * secondFraction.denominator,
	        denominator * secondFraction.numerator);
	        return result;
	    }
	    public String toString()
	    {
	        return "" + numerator + "/" + denominator;
	    }
	    public double toDecimal(double numerator, double denominator)
	    {
	        return numerator / denominator;
	    }
	    public void reduce()
	    {
	        int i = Math.min(Math.abs(numerator), Math.abs(denominator));
	        if(i == 0)
	            return;
	        while ((numerator % i != 0) || (denominator % i != 0))
	            i--;
	        if (numerator < 0 && denominator <0)
	        {
	            numerator = Math.abs(numerator);
	            denominator = Math.abs(denominator);
	        }
	        numerator = numerator / i;
	        denominator = denominator / i;
	    }
	    public int getNumerator()
	    {
	        return numerator;
	    }
	    public int getDenominator()
	    {
	        return denominator;
	    }
	    public String getSign()
	    {
	        if ((denominator < 0 && numerator > 0) || (numerator < 0 && denominator > 0))
	            return "-";
	        else if (numerator == 0)
	            return "No sign (zero)";
	        else
	            return "+";
	    }
	    
	    
	}


